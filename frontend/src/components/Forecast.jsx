import React from "react";
import ForecastDetails from "./ForecastDetails";

function Forecast({ forecast_input, forecast_date }) {
  //    Extract keys before JSX:
  //   const keys = Object.keys(forecast_input);

  console.log("forecast_input", forecast_input, "forecast_date", forecast_date);
  return (
    <div>
      <div className="flex items-center justify-center my-6">
        <p className="text-white font-medium uppercase">Forecast each 3h</p>
      </div>
      <div>
        <div>
          <div className="flex items-center justify-center my-2">
            <p className="text-white font-bold uppercase">{forecast_date}</p>
          </div>
          <div className="text-white font-light">
            {forecast_input[forecast_date].map((period_forecast) => {
              return (
                <ForecastDetails
                  period_forecast_input={period_forecast}
                  forecast_date={forecast_date}
                />
              );
            })}
          </div>
        </div>
      </div>
    </div>
  );
}

export default Forecast;
