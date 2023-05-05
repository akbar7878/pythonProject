for i in range(20):
        response = httpx.get(url='https://api.chucknorris.io/jokes/random')
        data = response.json()
        path = data['created_at'].split()[0]
        a, b, c = path.split('-')
        if a in os.listdir():
            os.chdir(a)
            if b in os.listdir():
                os.chdir(b)
                if c in os.listdir():
                    os.chdir(f"{os.getcwd().rsplit('/', 2)[0]}")
                else:
                    os.mkdir(c)
                    os.chdir(f"{os.getcwd().rsplit('/', 2)[0]}")
            else:
                os.mkdir(b)
                os.chdir(f"{os.getcwd().rsplit('/', 1)[0]}")
        else:
            os.mkdir(a)