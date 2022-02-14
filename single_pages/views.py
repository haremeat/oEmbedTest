from django.shortcuts import render, redirect
import oembed
import json
import os
import tldextract as tld



# Create your views here.
def index(request):
    return render(
        request,
        'single_pages/index.html',
    )


def result(request):
    url = request.POST.get('url')

    top_level_domain = tld.extract(url).domain

    # static 파일 열기
    simp_path = 'single_pages/static/providers.json'
    abs_path = os.path.abspath(simp_path)

    with open(abs_path, 'r') as f:
        providers_dict = json.load(f)

    # 데이터 가져오기
    for provider in providers_dict:
        if top_level_domain in provider['provider_url']:
            scheme_url = provider['endpoints'][0].get('schemes')[0]
            endpoint_url = provider['endpoints'][0].get('url')

            if tld == "instagram":
                endpoint_url = provider['endpoints'][0].get(
                    'url') + "?url=" + url + "&access_token=IGQVJVakw0RGdpLWtCR1JsbGRtTjhyRG1pYng3RTR1M1RaTE83WUJidzRpdldGSG1JRFVQNXdiejd3UVJVMXJwUzNvRW5uZAENGcnFEWjRHQzNydkRYelE4NmpGM0tQSkZA6WVgyUmVtUTEzSDNzQUN5cQZDZD"

    try:
        consumer = oembed.OEmbedConsumer()
        endpoint = oembed.OEmbedEndpoint(endpoint_url, \
                                         [scheme_url])

        consumer.addEndpoint(endpoint)
        response = consumer.embed(url)

        contents = response.getData()
    except:
        contents = {'error': 'F-1', 'url': url}

    return render(request, 'single_pages/result.html', contents)
