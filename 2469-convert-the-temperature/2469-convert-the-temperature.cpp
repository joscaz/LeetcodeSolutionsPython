class Solution {
public:

    double celsiusToFahrenheit(double celsius){
        double formula = celsius * 1.80 + 32.00;

        return formula;
    }

    double celsiusToKelvin(double celsius){
        double formula = celsius + 273.15;

        return formula;
    }

    vector<double> convertTemperature(double celsius) {
        vector<double> ans;

        ans.push_back(celsiusToKelvin(celsius));
        ans.push_back(celsiusToFahrenheit(celsius));

        return ans;
    }
};