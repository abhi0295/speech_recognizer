class KeyWord:
    wordList =['google','youtube','facebook','github','udemy','linkedin']
    def wordMatch(request):
        #split the words of the request in list
        requstToList = request.split()
        print(requstToList)
        for i in requstToList:
            if i in KeyWord.wordList:
                return i
        return None
    def searchQuery(self,request):
        query = ""
        if " " in request:
            request = request.split()
            request.remove("search")
            request.remove("about")
            query = "+".join(request)
            return query
