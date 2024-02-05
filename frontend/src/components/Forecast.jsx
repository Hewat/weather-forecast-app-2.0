import React from "react";
import ForecastDetails from "./ForecastDetails";

function Forecast({ forecast_input, forecast_date }) {
  return (
    <div>
      <div className="flex items-center justify-center my-6">
        <p className="text-white font-light uppercase">Forecast each 3h</p>
      </div>
      <div>
        <div>
          <div className="flex items-center justify-center my-1">
            <p className="text-white font-light text-xl uppercase">
              {forecast_date}
            </p>
          </div>
          <div className="text-white font-light">
            {forecast_input[forecast_date]["day_forecast_list"].map(
              (period_forecast) => {
                return (
                  <ForecastDetails
                    period_forecast_input={period_forecast}
                    forecast_date={forecast_date}
                  />
                );
              }
            )}
          </div>
        </div>
      </div>
    </div>
  );
}

export default Forecast;
