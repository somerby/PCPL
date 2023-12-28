def field(items, *args):
    assert len(args) > 0, 'Нужно указать хотя бы 1 ключ'
    if len(args) > 1:
        return [{j: i[j] for j in args if j in i and i[j] != None} for i in items]
    else:
        return [i[args[0]] for i in items if args[0] in i and i[args[0]] != None]

def main():
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
    ]
    print(str(field(goods, 'title'))[1:-1])
    print(str(field(goods, 'title', 'price'))[1:-1])

if __name__ == '__main__' :
    main()