class Logs:
    
    def process_request(self, request):
        try:
            print request.META['HTTP_MOZAIC_LOGS']
        except:
            pass
