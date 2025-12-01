import json

def main():
    with open("result.json","r",encoding="utf-8") as file:
        result = json.load(file)
    result = dict(sorted(result.items(),key = lambda x: x[1][0]/x[1][1]))
    for item in result:
        print(item,result[item],result[item][0]/result[item][1])


if __name__=="__main__":
    main()