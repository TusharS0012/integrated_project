import React from "react";
function Body() {
  return (
    <div className="bg-white h-full w-full">
      <div className="">
        <script
          type="module"
          src="https://prod-apnortheast-a.online.tableau.com/javascripts/api/tableau.embedding.3.latest.min.js"
        ></script>
        <tableau-viz
          id="tableau-viz"
          src="https://prod-apnortheast-a.online.tableau.com/t/22bcs061-15223ca96d/views/ExecutiveDashboard/ExecutiveDashboard"
          width="1650"
          height="840"
          toolbar="bottom"
        ></tableau-viz>
      </div>
    </div>
  );
}

export default Body;
