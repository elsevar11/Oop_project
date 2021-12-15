
class NoticeBoard:
    """
    This class contains the details of the noticeboard and its information.
    """
    def __init__(self):
        self.NewsList=list()
    def AddContent(self,News):
        self.NewsList.append(News)

    def Display(self):

        return self.NewsList



# n1=NoticeBoard()
#
# n1.AddContent("sa")
# n1.AddContent("as")
# n1.AddContent("assasld")
# print(n1.Display())



