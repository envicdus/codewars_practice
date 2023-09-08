'''
The year is 2070 and intelligent connected machines have replaced humans in most things. There are 
still a few critical jobs for mankind including machine software developer, for writing and maintaining 
the AI software, and machine forward deployed engineer for controlling the intelligent machines in the 
field. Lorimar is a forward deployed machine engineer and at any given time he controls thousands of BOT 
robots through real time interfaces and intelligent automation software. These interfaces are directly 
connected to his own brain so at all times his mind and the robots are one. They are pre-trained to think 
on their own but on occasion the human will direct the robot to perform a task.

There is an issue with the ultrasonic sensor data feed from BOT785 currently connected to Lorimar through
a real time interface. The data feed from sensor five should be a series of floats representing the relative
distance of objects within BOT785's path. The sensor error log has been saved for triage and Lorimar needs
to search through the data to determine the mean and standard deviation of the distance variables.

You will be given a list of tuples extracted from the sensor logs:

sensor_data = [('Distance:', 116.28, 'Meters', 'Sensor 5 malfunction =>lorimar'), 
('Distance:', 117.1, 'Meters', 'Sensor 5 malfunction =>lorimar'), 
('Distance:', 123.96, 'Meters', 'Sensor 5 malfunction =>lorimar'), 
('Distance:', 117.17, 'Meters', 'Sensor 5 malfunction =>lorimar')]
Return a tuple with the mean and standard deviation of the distance variables rounded to 
four decimal places. The variance should be computed using the formula for samples (dividing by N-1).

|Mean| |Standard Deviation|

(118.6275, 3.5779)
Hint (http://math.stackexchange.com/questions/15098/sample-standard-deviation-vs-population-standard-deviation)

Please also try the other Kata in this series..
'''

# my solution

def sensor_analysis(sensor_data):
    distances = [x[1] for x in sensor_data]
    mean_distances = round(sum(distances)/len(distances), 4)
    deviation_mean = [(mean_distances - m)**2 for m in distances]
    sample_st_dv = round((sum(deviation_mean)/(len(distances)-1))**(0.5), 4)
    return (mean_distances, sample_st_dv)

# other solution

# 1

from numpy import mean,std

def sensor_analysis(sensor_data):
    data = [data[1] for data in sensor_data]
    return ( round(mean(data),4), round(std(data, ddof=1),4) )

# 2

def sensor_analysis(data):
    data = [x[1] for x in data]
    
    mean  = sum(data) / len(data)
    
    std_dev = (sum((x - mean) ** 2 for x in data) / (len(data) - 1)) ** 0.5
    
    return round(mean, 4) , round(std_dev, 4)

# 3

from statistics import mean, stdev

def sensor_analysis(data):
    dists = [log[log.index('Distance:') + 1] for log in data]
    return round(mean(dists), 4), round(stdev(dists),  4)