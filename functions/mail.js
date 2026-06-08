export async function onRequestPost({ request, env }) {
  try {
    const data = await request.formData();
    const name = data.get('name');
    const phone = data.get('phone');
    const message = data.get('message');

    // Wir nutzen jetzt Resend statt MailChannels. 
    // ACHTUNG: Der RESEND_API_KEY muss im Cloudflare Dashboard hinterlegt werden!

    const emailHtml = `
      <div style="font-family: sans-serif; max-width: 600px; padding: 20px; border: 1px solid #e1e1e1; border-radius: 8px;">
        <h2 style="color: #ea580c; border-bottom: 2px solid #ea580c; padding-bottom: 10px;">Neuer Lead: Drehmoment Digital</h2>
        <p><strong>Name / Betrieb:</strong> ${name}</p>
        <p><strong>Telefonnummer:</strong> ${phone}</p>
        <p><strong>Nachricht:</strong><br>${message}</p>
        <hr style="border: 0; border-top: 1px solid #eee; margin: 20px 0;">
        <p style="font-size: 12px; color: #666;">Gesendet via Drehmoment Digital Website (Cloudflare Pages Worker & Resend Integration)</p>
      </div>
    `;

    const resend_request = await fetch('https://api.resend.com/emails', {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${env.RESEND_API_KEY}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        from: 'Drehmoment Leads <leads@drehmoment-digital.de>',
        to: ['kontakt@drehmoment-digital.de'],
        subject: `NEUE ANFRAGE: ${name}`,
        html: emailHtml,
      }),
    });

    const res = await resend_request.json();

    if (resend_request.ok) {
      return new Response(JSON.stringify({ success: true, id: res.id }), {
        headers: { 'Content-Type': 'application/json' },
      });
    } else {
      return new Response(JSON.stringify({ success: false, error: res.message || 'Resend API Fehler' }), {
        status: 500,
        headers: { 'Content-Type': 'application/json' },
      });
    }

  } catch (err) {
    return new Response(JSON.stringify({ success: false, error: err.message }), {
      status: 500,
      headers: { 'Content-Type': 'application/json' },
    });
  }
}
