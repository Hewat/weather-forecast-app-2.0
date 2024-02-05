import React from "react";
// @ts-ignore
import { UilTemperature, UilTear, UilWind } from "@iconscout/react-unicons";

function ForecastDetails({ period_forecast_input, forecast_date }) {
  console.log(
    "period_forecast_input",
    period_forecast_input,
    "key",
    forecast_date
  );
  return (
    <div>
      <div className="flex flex-row items-center gap-4 my-3">
        <div className="flex w-36 justify-end">
          <div className="items-center mr-1 text-sm">
            {period_forecast_input.datetime.time}
          </div>
        </div>
        <div className="flex border border-gray-300 rounded gap-2 w-full">
          <div className="flex items-center">
            <img
              src={period_forecast_input.icon_url}
              className="w-6 my-1"
              alt=""
            />
            <div className="flex w-10 text-xs">
              {period_forecast_input.main_description}
            </div>
            <div className="flex w-20 text-sm justify-center">
              {period_forecast_input.forecast_temp} °C
            </div>
          </div>
          <div className="flex w-32 items-center">
            <div className="font-light ml-1 text-xs">feels like</div>
            <div className="flex ml-1">
              <div className="flex items-center text-sm ">
                <UilTemperature size={13} className="mr-1" />
                {period_forecast_input.feels_like_temp} °C
              </div>
            </div>
          </div>
          <div className="flex w-24 items-center text-xs">
            <UilWind size={13} className="ml-3" />
            <div className="flex items-center">
              {period_forecast_input.wind_speed} km/h
            </div>
          </div>
          <div className="flex items-center">
            <UilTear size={13} className="mr-1" />
            <div className="flex w-10 items-center text-sm">
              {period_forecast_input.humidity} %
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default ForecastDetails;
