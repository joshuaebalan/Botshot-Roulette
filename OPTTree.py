class Node:

   live = 0

   blank = 0

   turn = True #true for player turn, false for dealer turn

   score = 0
   liveProb = 0.0
   blankProb = 0.0
   
   liveChild = None
   blankChild = None

   def __init__(live, blank, turn):
       self.live = live
       self.blank = blank
       self.turn = turn
       self.liveProb = live / (live + blank)
       self.blankProb = blank / (live + blank)
       if self.blankProb > 0:
           if self.blankProb > 0.5:
               self.blankChild = Node(live, (blank - 1), turn) #shot self, and shot was blank; player maintains control
           else:
               self.blankChild = Node(live, (blank - 1), (not turn)) #did not shoot self, shot was blank, player loses control
       if self.liveProb > 0:   
           if self.liveProb >= 0.5: #shot opponent, shot was live
                self.liveChild = Node((live - 1), blank, (not turn)) 
           else: #shot self, shot was live
                self.liveChild = Node((live - 1), blank, (not turn))
       self.score = Score(self)

   def Score(node) -> float:
       if node.live == 0: #base case: only blanks left
           return 0
       if node.liveChild is None and node.blankChild is None: #base case: last shot in the gun
           if node.live == 1: #last bullet is live
               if node.turn: #if true, it's the player's turn
                   return 1 #player shoots dealer
               else: #if not, it's the dealer's turn
                   return -1 #dealer shoots player
           return 0
       #otherwise, we recurse and dynamically calculate the score
       liveScore = 0
       blankScore = 0
       if node.liveChild is not None:
           if node.liveChild.turn:
               liveScore = node.liveProb * Score(node.liveChild) #it is player's turn
           else:
               liveScore = node.liveProb * -1 * Score(node.liveChild) #it is opponent's turn
       if node.blankChild is not None:
           if node.blankChild.turn:
               blankScore = node.blankProb * Score(node.blankChild)
           else:
               blankScore = node.blankProb * Score(node.blankChild)
       return liveScore + blankScore


