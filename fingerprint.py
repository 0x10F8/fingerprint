    import json
    import hashlib

    def lambda_handler(event, context):
        
        # Get the headers and the request body
        headers = event['headers']
        body = json.loads(event['body'])

        # Get the fingerprint information
        accept = headers['accept']
        accept_encoding = headers['accept-encoding']
        accept_language = headers['accept-language']
        user_agent = headers['User-Agent']
        ip = headers['X-Forwarded-For']
        resolution = body['resolution']
        image_data = body['imageData']
        plugins = body['plugins']
        platform = body['platform']
        cookies_enabled = body['cookiesEnabled']
        do_not_track = body['doNotTrack']
        timezone = body['timezone']
        web_gl_renderer = body['webGLRenderer']

        # Put the collected information into a dictionary
        collected_information = {
            'Accept': accept,
            'Accept-Encoding': accept_encoding,
            'Accept-Language': accept_language,
            'User-Agent': user_agent,
            'IP': ip,
            'Resolution': resolution,
            'ImageData': image_data,
            'Plugins': plugins,
            'Platform': platform,
            'CookiesEnabled': cookies_enabled,
            'DoNotTrack': do_not_track,
            'TimezoneOffset': timezone,
            'WebGLRenderer': web_gl_renderer
        }

        # Create a hash with the information
        m = hashlib.sha256()
        m.update(accept.encode('utf8'))
        m.update(accept_encoding.encode('utf8'))
        m.update(accept_language.encode('utf8'))
        m.update(user_agent.encode('utf8'))
        m.update(ip.encode('utf8'))
        m.update(resolution.encode('utf8'))
        m.update(image_data.encode('utf8'))
        m.update(plugins.encode('utf8'))
        m.update(platform.encode('utf8'))
        m.update(cookies_enabled.encode('utf8'))
        m.update(do_not_track.encode('utf8'))
        m.update(timezone.encode('utf8'))
        m.update(web_gl_renderer.encode('utf8'))

        hashed = m.hexdigest()
        collected_information['hash'] = hashed

        print(collected_information)

        # Return the data
        return {
            'statusCode': 200,
            'headers': {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "Content-Type",
                "Access-Control-Allow-Methods": "OPTIONS,POST",
                "Content-Type" : "application/json"
            },
            'body': json.dumps(collected_information, indent=True)
        }
