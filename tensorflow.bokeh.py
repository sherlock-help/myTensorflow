import psycopg2
from bokeh.plotting import figure, output_file, show

#defined function here
def drawChar(cur, sDeptName, sDoctorName, p):
    cur.execute("select * from five_number where \"DeptName\"='"+
                sDeptName +"' and \"DoctorName\" = '"+ sDoctorName +"'")
    rows = cur.fetchall()

    xThisHour = []
    yThisNumber = []
    xNextHour = []
    xNextNumber = []
    for row in rows: 
        if 0 == row[8]:
            continue
        if("本周" == row[2]):
            xThisHour.append(int(row[7]))
            yThisNumber.append(int(row[6]))
        elif("下周" == row[2]):
            xNextHour.append(int(row[7]))
            xNextNumber.append(int(row[6]))
        
        
        #0:科室;1:医生姓名;2:周次;3:周几;4:日期;6:号源;7:小时;8:数据是否生效
        #print(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7])
        

    #xHour.append(1)
    #xHour.append(2)
    #xHour.append(3)

    #yNumber.append(0)
    #yNumber.append(65)
    #yNumber.append(78)

    #draw a point
    p.circle(
        xThisHour,
        yThisNumber,
        size=3, color="green", alpha=0.5)
    p.circle(
        xNextHour,
        xNextNumber,
        size=3, color="red", alpha=0.5)
 




# output to static HTML file
output_file("five_number.bokeh.html")

# create a new plot
p = figure(
   #tools="pan,box_zoom,reset,save",
   y_axis_type="log", y_range=[0.1, 10**3/2], x_range=[0.01, 24],
   title="第五医院号源采集智能比对系统",
   x_axis_label='每天小时计算', y_axis_label='号源')



#get data here
conn = psycopg2.connect(database="xmsmjk.com", user="postgres", password="root", host="localhost", port="5432")
cur = conn.cursor()
cur.execute("select distinct \"DeptName\", \"DoctorName\" from five_number")
rows = cur.fetchall()
#select the distinct detpname and doctor name
for row in rows: 
    drawChar(cur, row[0], row[1], p)
    
#show the resultsshow(p)
show(p)
