import webbrowser as wb
import net_connect_validator
import word_search

class Activities:
    def activityManger(self, request):
        request = request.lower()
        if 'open' in request:
            return Activities().Open(request)

    def Open(self,request):
        try:
            url, last = "https://", ".com"
            key_word = word_search.KeyWord.wordMatch(request)
            print(key_word)
            if key_word is None:
                return "sorry, request cannot be proceed"
            else:
                url = url+key_word+last
                while net_connect_validator.checkConnectivity():
                    wb.get().open_new(url)
                    return "opening "+key_word
                return "Sorry, Please check network connection"
        except:
            print(Exception)
