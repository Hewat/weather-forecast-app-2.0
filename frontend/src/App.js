import "./App.css";
import UilReact from "@iconscout/react-unicons/icons/uil-react";
import TopButtons from "./components/TopButtons";
import React, { useEffect, useState } from "react";
import Inputs from "./components/Inputs";
import TimeAndLocation from "./components/TimeAndLocation";
import TemperatureAndDetails from "./components/TemperatureAndDetails";
import Forecast from "./components/Forecast";
import getWeatherData from "./services/weatherService";
import DayCard from "./components/DayCard";

function App() {
  // setting states
  const [city, setCity] = useState("São Paulo");
  const [weather, setWeather] = useState(null);
  const [showForecast, setShowForecast] = useState(false);
  const [selectedForecastDate, setSelectedForecastDate] = useState("");

  useEffect(() => {
    const fetchWeatherData = async (city) => {
      await getWeatherData(city).then((data) => {
        setWeather(data);
      });
    };

    fetchWeatherData(city);
  }, [city]);

  function openForecast(selectedDate) {
    setShowForecast(true);
    setSelectedForecastDate(selectedDate);
  }

  const formatBackgroundColor = () => {
    if (!weather) return "from-cyan-700 to-blue-700";
    const threshold = 20;
    if (weather.current_weather.current_temp <= threshold) {
      return "from-cyan-400 to-blue-700";
    } else return "from-yellow-400 to-orange-600";
  };

  return (
    <div
      className={`mx-auto max-w-screen-md mt-4 py-5 px-32 bg-gradient-to-br ${formatBackgroundColor()} h-fit shadow-xl shadow-gray-400`}
    >
      <TopButtons setCity={setCity} />
      <Inputs setCity={setCity} />

      {weather && city !== "" && (
        <div>
          <TimeAndLocation weather_input={weather} />
          <TemperatureAndDetails weather_input={weather.current_weather} />

          <div className="forecast-container">
            {Object.keys(weather.forecast).map((forecastDate) => (
              <DayCard
                key={forecastDate}
                weekday={forecastDate}
                maxTemp={weather.forecast[forecastDate].max_day_temp}
                minTemp={weather.forecast[forecastDate].min_day_temp}
                handleClick={() => openForecast(forecastDate)}
              />
            ))}

            {showForecast && (
              <Forecast
                forecast_date={selectedForecastDate}
                forecast_input={weather.forecast}
              />
            )}
          </div>
        </div>
      )}
    </div>
  );
}

export default App;
