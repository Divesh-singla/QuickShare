import sys
sys.path.insert(0,r'S:\ACIL\project\schoolCRM')
from mysqlConnection.connection import getConnection

sql = getConnection()

def __getPageSlug(title, insertId  , tableName , titleColumnName ):

    count = 0
    slugFetchQuery = f"SELECT {titleColumnName} FROM {tableName}"
    sql.execute(slugFetchQuery)
    slugFetchResult = sql.fetchall()
    # print(slugFetchResult[0])

    for x in slugFetchResult:
        # print(x[0])
        if x[0] != None and (x[0].lower()) == title.lower():
            print(x[0])
            count += 1
    print("vounttttttttttttttttttttttttttt",count)

    if count <= 1:
        title = (title.lower()).replace(" ","-")
    else:
        title = ((title.lower()).replace(" ","-")) + f"-{insertId}"

    return title
