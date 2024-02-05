import "./App.css";
import UilReact from "@iconscout/react-unicons/icons/uil-react";
import TopButtons from "./components/TopButtons";
import React, { useEffect, useState } from "react";
import Inputs from "./components/Inputs";
import TimeAndLocation from "./components/TimeAndLocation";
import TemperatureAndDetails from "./components/TemperatureAndDetails";
import Forecast from "./components/Forecast";
import getWeatherData from "./services/weatherService";

function App() {
  // setting states
  const [city, setCity] = useState("Campo Mourão");
  const [weather, setWeather] = useState(null);

  useEffect(() => {
    const fetchWeatherData = async (city) => {
      await getWeatherData(city).then((data) => {
        console.log("DATA WEATHER", data);
        setWeather(data);
      });
    };

    fetchWeatherData(city);
  }, [city]);

  return (
    <div className="mx-auto max-w-screen-md mt-4 py-5 px-32 bg-gradient-to-br from-cyan-700 to-blue-700 h-fit shadow-xl shadow-gray-400">
      <TopButtons />
      <Inputs />

      {weather && (
        <div>
          <TimeAndLocation weather_input={weather} />
          <TemperatureAndDetails weather_input={weather.current_weather} />
          <Forecast
            forecast_input={weather.forecast}
            forecast_date="07/02/2024"
          />
        </div>
      )}
    </div>
  );
}

export default App;
