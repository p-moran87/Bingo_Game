import random
import time

numbers = range(1, 91, 1)

dict_bingo = {1: "Kelly's Eye --1", 2: "One little duck --2", 3: "Cup of Tea --3", 4: "Knock at the door --4", 5: "Man Alive --5", 6: "Tom Mix --6",
				7: "Lucky number 7", 8: "Garden Gate --8", 9: "Take a line --9", 10: "Downing Street --10", 11: "Legs Eleven --11", 12: "One dozen --12",
				13: "Unlucky for some --13", 14: "The Lawnmover --14", 15: "Young and Keen --15", 16: "Never been kissed --16", 17: "Dancing Queen -17", 18: "Coming of Age --18",
				19: "Goodbye Teens --19", 20: "One score --20", 21: "Key of the door --21", 22: "Two little ducks --22", 23: "The lord is my shepard --23", 24: "Two dozen --24",
				25: "Duck and dive --25", 26: "2 and 6 --26", 27: "Duck and crutch --27", 28: "In a state --28", 29: "Rise and shine --29", 30: "Dirty Gertie --30",
				31: "Get up and run --31", 32: "Buckle my shoe --32", 33: "All the threes --33", 34: "Ask for more --34", 35: "Jump and jive --35", 36: "Triple dozen --36",
				37: "3 and 7 --37", 38: "Christmas cake --38", 39: "3 and 9 --39", 40: "Life begins --40", 41: "4 and 1 --41", 42: "4 and 2 --42", 
				43: "Down on your knees --43", 44: "Droopy drawers --44", 45: "Halfway there --45", 46: "Up to tricks --46", 47: "4 and 7 --47", 48: "Four dozen --48",
				49: "PC --49", 50: "Bullseye! --50", 51: "5 and 1 --51", 52: "Deck of cards --52", 53: "Here comes Herbie --53", 54: "5 and 4 --54",
				55: "All the fives --55", 56: "5 and 6 --56", 57: "Heinz beans --57", 58: "A long wait --58", 59: "5 and 9 --59", 60: "3 Score --60", 
				61: "6 and 1 --61", 62: "Tickety boo --62", 63: "Katie's bad knee --63", 64: "Almost retired --64", 65: "Retirement age --65", 66: "Clickety click --66",
				67: "Stairway to heaven --67", 68: "Pick a mate --68", 69: "6 and 9 --69", 70: "7 tens --70", 71: "Bang on the drum -- 71", 72: " Danny la rue --72",
				73: "Queen bee --73", 74: "Hit the floor --74", 75: "7 and 5 --75", 76: "Trombones --76", 77: "Sunset strip --77", 78: "39 more steps --78",
				79: "7 and 9 --79", 80: "Ate nothing --80", 81: "8 and 1 --81", 82: "8 and 2 --82", 83: "Time for tea --83", 84: "Seven dozen --84",
				85: "Staying alive --85", 86: "Between the sticks --86", 87: "8 and 7 --87", 88: "Two fat ladies --88", 89: "Almost there --89", 90: "Top of the shops --90"}

random.shuffle(numbers)
# print out the values in the dictionary using the indices of the shuffled list of numbers as the input keys


while True:
        try:
            ## Keep doing something here
            for i in range(0, 90):
				print(dict_bingo.get(numbers[i]))
				time.sleep(7)

        except KeyboardInterrupt:
            ## write or call pause function which could be time.sleep()
            print '\nPausing...  (Hit ENTER to continue, type quit to exit.)'
            try:
                response = raw_input()
                if response.lower() == 'quit':
                    break
                print 'Quitting...'
            except KeyboardInterrupt:
                print 'Resuming...'
                continue


