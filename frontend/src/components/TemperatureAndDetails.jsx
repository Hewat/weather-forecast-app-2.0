// @ts-nocheck
import React from "react";
import {
  UilArrowUp,
  UilArrowDown,
  UilTemperature,
  UilTear,
  UilWind,
  UilSun,
  UilSunset,
} from "@iconscout/react-unicons";

function TemperatureAndDetails({
  weather_input: {
    description,
    icon_url,
    current_temp,
    feels_like_temp,
    humidity,
    wind_speed,
    sunrise_time,
    sunset_time,
    max_day_temp,
    min_day_temp,
  },
}) {
  return (
    <div>
      <div className="flex items-center justify-center py-6 text-xl text-cyan-300">
        <p>{description}</p>
      </div>

      <div className="flex flex-row items-center justify-between text-white py-3">
        <img className="w-20" src={icon_url} alt="" />
        <p className="text-5xl">{current_temp}°C</p>
        <div className="flex flex-col space-y-2">
          {/* Real Feel */}
          <div className="flex font-light text-sm items-center justify-center">
            <UilTemperature size={18} className="mr-1" />
            Real fell:
            <span className="font-medium ml-1">{feels_like_temp}°C</span>
          </div>
          {/* Humidity */}
          <div className="flex font-light text-sm items-center justify-center">
            <UilTear size={18} className="mr-1" />
            Humidity:
            <span className="font-medium ml-1">{humidity}%</span>
          </div>
          {/* Wind Speed */}
          <div className="flex font-light text-sm items-center justify-center">
            <UilWind size={18} className="mr-1" />
            Wind:
            <span className="font-medium ml-1">{wind_speed} km/h</span>
          </div>
        </div>
      </div>
      {/* Aditional Weather Data */}
      <div className="flex from-row items-center justify-center space-x-2 text-white text-sm py-3">
        <UilSun />
        <p className="font-light">
          Rise: <span className="font-medium ml-1">{sunrise_time.time}</span>
        </p>
        <UilSunset />
        <p className="font-light">
          Set: <span className="font-medium ml-1">{sunset_time.time}</span>
        </p>
        <p className="font-light">|</p>
        <UilArrowUp />
        <p className="font-light">
          High: <span className="font-medium ml-1">{max_day_temp}</span>
        </p>
        <p className="font-light">|</p>
        <UilArrowDown />
        <p className="font-light">
          Low: <span className="font-medium ml-1">{min_day_temp}</span>
        </p>
      </div>
    </div>
  );
}

export default TemperatureAndDetails;
