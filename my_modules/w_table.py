# here is a web table
def table(rows, cols):
    t = {'rows':rows, 'cols':cols}
    return t

if __name__ == '__main__':
    # exercise this module
    web_t = table(300, 200)
    print(web_t)
