def run(input, output):
    class Person:
        def __init__(self, firstName, lastName, idNumber):
            self.firstName = firstName
            self.lastName = lastName
            self.idNumber = idNumber

        def printPerson(self):
            print("Name:", self.lastName + ",", self.firstName)
            print("ID:", self.idNumber)

    class Student(Person):
        #   Class Constructor
        #
        #   Parameters:
        #   firstName - A string denoting the Person's first name.
        #   lastName - A string denoting the Person's last name.
        #   id - An integer denoting the Person's ID number.
        #   scores - An array of integers denoting the Person's test scores.
        #
        # Write your constructor here
        def __init__(self, firstName, lastName, idNumber, scores):
            Person.__init__(self, firstName, lastName, idNumber)
            self.score = scores

        #   Function Name: calculate
        #   Return: A character denoting the grade.
        #
        # Write your function here
        def calculate(self):
            sum_scores = sum(scores)
            if sum_scores/len(scores)   >= 90 and sum_scores/len(scores) <=100:
                return ('O')
            elif sum_scores/len(scores) >= 80 and sum_scores/len(scores) <90:
                return ('E')
            elif sum_scores/len(scores) >= 70 and sum_scores/len(scores) <80:
                return ('A')
            elif sum_scores/len(scores) >= 55 and sum_scores/len(scores) <70:
                return ('P')
            elif sum_scores/len(scores) >= 40 and sum_scores/len(scores) <55:
                return ('D')
            elif sum_scores/len(scores)  < 40:
                return ('T')

    f = open(input, 'r')
    wr = open(output, 'w')
    input_info = f.readline().rstrip('\n').split(" ")
    firstName = input_info[0]               # TODO in python, we dont use uppercase in variable like C#.
                                            #      please read for more information ref. https://stackoverflow.com/questions/159720/what-is-the-naming-convention-in-python-for-variable-and-function-names
                                            #      please install pep8 to follow coding convention.
    lastName = input_info[1]
    idNum = input_info[2]
    numScore = int(f.readline())            # TODO redundant variable
    scores = list(map(int, f.readline().split()))
    s = Student(firstName, lastName, idNum, scores)
    s.printPerson()
    print("Grade:", s.calculate())


if __name__ == '__main__':
    run('input.txt','output.txt')

# TODO noone create Class inside function
