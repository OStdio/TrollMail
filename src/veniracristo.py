
def venir_a_cristo_data(email: str, phone_number: str) -> dict:

    country_code, number = phone_number.split()

    with open("src\country_codes.txt", "r") as country:
        country_code = country_code.replace(" ", "")
        content = country.read()
        countries = content.split("\n")
        for country in countries:
            country_iso3, country_number, country_name = country.split(":")
            if country_number == country_code:
                pass
            
        print(country_name)
    return {
        "firstName": "Tom",
        "lastName": "Parker",
        "email": email,
        "subscriptions": "mDGLSPAInspirationSubscribed",
        "country": "",
        "locID": "",
        "countryISO3": "",
        "addr": "",
        "city": "",
        "state": "",
        "zip": "101010",
        "phoneCountryCode": country_code,
        "phone": number,
        "phoneCountry": "cr",
        "offerType": "meetWithMissionaries",
        "customWhitelist": "true",
        "formType": "request",
        "lang": "spa",
        "preferredLanguageId": "2",
        "countryIso2": "undefined",
        "successPageURL": "*!veniracristo!success!spa!published",
        "cancelPageURL": "*!veniracristo!cancel!spa!published",
        "formTopicId": "2c54b042-6c2c-4ed0-927e-2919b627a551",
        "system_source": "ComeUntoChrist",
        "submittingURL": "https://www.veniracristo.org/",
        "pageTitle": "Bienvenido | veniracristo",
        "offerId": "134",
        "sourceId": "5502",
        "offerType": "meetWithMissionaries",
        "munchkinId": "",
        "marketoToken": "", 
        "domain": "www.veniracristo.org",
        "offerDetails": """[{"description":"¿Cómo prefieres que te contactemos?","text":"¿Cómo prefieres que te contactemos?","type":"MULTI_SELECT","options":["Llamada telefónica","Mensaje de WhatsApp","Mensaje de texto"],"availableDate":"2020-01-13T15:00:00","endDate":"2024-12-31T23:59:59","userEditableOption":false,"missionaryEditable":true,"sortOrder":"8","locale":"spa","questionGuid":"8d544658-2c0f-4030-93e2-03e19c1996f5","selected":["Llamada telefónica","Mensaje de WhatsApp","Mensaje de texto"]},{"description":"Por favor, confirma - missionaries","text":"Por favor, confirma:","type":"MULTI_SELECT","options":["Entiendo que los misioneros se pondrán en contacto conmigo para responder a mis preguntas y compartir un mensaje edificante."],"availableDate":"2020-05-13T15:00:00","userEditableOption":false,"missionaryEditable":false,"sortOrder":"1","locale":"spa","questionGuid":"07ff6313-f364-4a18-8ff4-d5d25cb4ee7e","selected":["Entiendo que los misioneros se pondrán en contacto conmigo para responder a mis preguntas y compartir un mensaje edificante."]}]""",
        "transactionId": "16870503377102267",
        "hashed": "2908ec72",
        "adobeVisitorId": "" ,
        "MDCampaignId": "10",
        "boncomCampaignId": "0"
    }

if __name__ == '__main__':
    venir_a_cristo_data("none", "+506 83427721")