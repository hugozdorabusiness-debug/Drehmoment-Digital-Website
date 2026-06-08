export default {
  async fetch(request, env) {
    // CORS-Header einrichten, damit das Skript von deiner Website aus aufgerufen werden darf
    const corsHeaders = {
      "Access-Control-Allow-Origin": "*", // Später hier deine echte Domain eintragen, z.B. "https://drehmoment-digital.de"
      "Access-Control-Allow-Methods": "POST, OPTIONS",
      "Access-Control-Allow-Headers": "Content-Type",
    };

    // Preflight-Request für CORS abfangen (macht der Browser automatisch vor dem eigentlichen Senden)
    if (request.method === "OPTIONS") {
      return new Response(null, { headers: corsHeaders });
    }

    // Wir akzeptieren nur POST-Anfragen (das Formular sendet Daten)
    if (request.method !== "POST") {
      return new Response("Method Not Allowed", { status: 405, headers: corsHeaders });
    }

    try {
      // Die Daten aus dem Formular auslesen, die als JSON geschickt werden
      const formData = await request.json();
      const { name, phone, message } = formData;

      // Überprüfen, ob die wichtigsten Felder ausgefüllt sind
      if (!name || (!phone && !message)) {
        return new Response(JSON.stringify({ error: "Bitte fülle die Pflichtfelder aus." }), {
          status: 400,
          headers: { "Content-Type": "application/json", ...corsHeaders },
        });
      }

      // Hier wird die E-Mail an Zoho gesendet. Wir nutzen z.B. einen Dienst wie Resend.com 
      // (Einfachste Methode, um Mails über eine API zu verschicken)
      const resendApiKey = env.RESEND_API_KEY; // Diesen Key hinterlegen wir später in Cloudflare

      const emailResponse = await fetch("https://api.resend.com/emails", {
        method: "POST",
        headers: {
          "Authorization": `Bearer ${resendApiKey}`,
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          from: "Website Anfrage <info@drehmoment-digital.de>", // Deine Absender-Adresse (muss bei Resend verifiziert sein)
          to: "info@drehmoment-digital.de", // Deine Empfänger-Adresse (Dein Zoho Postfach)
          subject: `Neue Projektanfrage von: ${name}`,
          html: `
            <h2>Neue Anfrage über die Website</h2>
            <p><strong>Name/Firma:</strong> ${name}</p>
            <p><strong>Telefon:</strong> ${phone || 'Nicht angegeben'}</p>
            <p><strong>Nachricht:</strong><br/>${message || 'Keine Nachricht hinterlassen'}</p>
          `
        })
      });

      if (!emailResponse.ok) {
        throw new Error("Fehler beim Senden der E-Mail durch den Drittanbieter.");
      }

      // Erfolgreiche Antwort an deine Website zurücksenden
      return new Response(JSON.stringify({ success: "Nachricht erfolgreich gesendet!" }), {
        status: 200,
        headers: { "Content-Type": "application/json", ...corsHeaders },
      });

    } catch (error) {
      // Fehlermeldung, falls etwas schiefgeht
      return new Response(JSON.stringify({ error: "Serverfehler: Die Nachricht konnte nicht verarbeitet werden." }), {
        status: 500,
        headers: { "Content-Type": "application/json", ...corsHeaders },
      });
    }
  }
};
