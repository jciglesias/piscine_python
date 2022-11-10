kata = {'Python': 'Guido van Rossum', 'Ruby': 'Yukihiro Matsumoto', 'PHP': 'Rasmus Lerdorf'}
# kata = {'Python': 'Guido van Rossum', 'Ruby': 'Yukihiro Matsumoto', 'PHP': 'Rasmus Lerdorf', 'C++': 'Bjarne Stroustrup'}
# kata = {}
if __name__=='__main__':
    for i in range(len(kata)):
        print(list(kata.keys())[i],"was created by", list(kata.values())[i]);