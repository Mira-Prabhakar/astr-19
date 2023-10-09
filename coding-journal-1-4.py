class Dog:

    def __init__(self, length_arm, length_legs, num_eyes, tail, furry):
        self.length_arm = length_arm
        self.length_legs = length_legs
        self.num_eyes = num_eyes
        self.tail = tail
        self.furry = furry

    def describe_dog(self):
        check_tail = ""
        check_furry = ""
        if self.tail == True:
            check_tail = "The dog has a tail. "
        else:
            check_tail = "The dog does not have a tail. "

        if self.furry == True:
            check_furry = "The dog is furry. "
        else:
            check_furry = "The dog is not furry. "
        print("The length of the dog's arms are " + str(self.length_arm) + " and the length of the legs are "
              + str(self.length_legs) + ". " + check_tail +
              "The dog has " + str(self.num_eyes) + " eyes. " + check_furry)



juno = Dog(2.5, 2.5, 2, True, True)
juno.describe_dog()
