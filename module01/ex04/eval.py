class Evaluator:
    def zip_evaluate(coefs: list, words: list):
        if type(coefs) is not list or type(words) is not list or len(words) != len(coefs):
            return -1
        sum = 0
        for word, coef in zip(words, coefs):
            if type(word) is not str:
                return -1
            sum += len(word) * float(coef)
        return sum
    def enumerate_evaluate(coefs: list, words: list):
        if type(coefs) is not list or type(words) is not list or len(words) != len(coefs):
            return -1
        sum = 0
        for i, (word, coef) in enumerate(zip(words, coefs)):
            if type(word) is not str:
                return -1
            sum += len(word) * float(coef)
        return sum

if __name__=="__main__":
    words = ["Le", "Lorem", "Ipsum", "est", "simple"]
    coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
    print(Evaluator.enumerate_evaluate(coefs, words))