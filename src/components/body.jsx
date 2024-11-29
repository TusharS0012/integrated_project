import React from "react";
function Body() {
  return (
    <div className="bg-white h-full w-full">
      <div className="">
        <tableau-viz
          id="tableau-viz"
          src="https://prod-apnortheast-a.online.tableau.com/t/22bcs098-7dbc0806ed/views/CORPORATE20FINANCE20-20Budget20Controlling/ExecutiveSummary"
          width="1300"
          height="840"
          hide-tabs
          toolbar="no-toolbar"
        ></tableau-viz>
      </div>
    </div>
  );
}

export default Body;
