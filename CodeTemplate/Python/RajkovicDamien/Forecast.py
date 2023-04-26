class Forecast:
    
    def __init__(self, rainfall, descriptors):
        self.rainfall = rainfall
        self.descriptors = descriptors

    def prepare_data(self):
        for day in range(len(self.rainfall[0])):
            for station in range(len(self.rainfall)):
                if self.rainfall[station][day] < 0:
                    if self.descriptors[day] == "sunny":
                        self.rainfall[station][day] = 0
                    elif self.descriptors[day] == "rainy":
                        # Ich habe ChatGTP gefragt, wie man das macht #
                        
                        valid_values = [val for val in self.rainfall if val == 0]
                        if len(valid_values) > 0:
                            avg = sum(valid_values) // len(valid_values)
                            self.rainfall[station][day] = avg
                        else:
                            self.rainfall[station][day] = 0
                        ###############################################

                    elif self.descriptors[day] == "thunderstorm":
                        self.rainfall[station][day] = abs(self.rainfall[station][day])
        return self.rainfall

    def total_rainfall(self):
       return sum([sum(row) for row in self.rainfall])


    def trend(self, n):
        average_rainfall = 0
        for i in range(n - len(self.rainfall[0])):
            for n in range(len(self.rainfall)):
                average_rainfall = average_rainfall + self.rainfall[i][n]
        if average_rainfall < 50:
            return "sunny"
        elif average_rainfall == 75:
            return "thunderstorm"
        else:
            return "rainy"


rainfall = [[3, 7, 2, -1, 0, 49], [2, -2, 6, 1, -1, -5]]
descriptors = ['sunny', 'rainy', 'sunny', 'rainy', 'sunny', 'thunderstorm']

forecast = Forecast(rainfall, descriptors)
print(forecast.prepare_data())
print(forecast.total_rainfall())
print(forecast.trend(7))

