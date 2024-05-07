console.log(">>> content-script activated <<<");

contribution_calendar = document.querySelector(".ContributionCalendar-grid");
calendar_body = contribution_calendar.querySelector("tbody");
rows = calendar_body.querySelectorAll("tr");
no_rows = rows.length;
no_cols = rows[0].querySelectorAll(".ContributionCalendar-day").length - 1;

console.log(`calendar dimensions: ${no_rows}x${no_cols}`);

fetch(`http://127.0.0.1:5000/raccoon?cal_dim=${no_rows}-${no_cols}`, {
    method: 'GET'
})
    .then(response => response.json())
    .then(async chart_data => {
        for (const frame in chart_data) {
            // console.log(chart_data[frame]);
            for (let y = 0; y < no_rows; y++) {
                for (let x = 0; x < no_cols; x++) {
                    rows[y].querySelectorAll(".ContributionCalendar-day")[x].setAttribute("data-level", chart_data[frame][`${x}x${y}`]);
                }
            }
            await delay(300);
        }
    })
    .catch(err => console.error(err));

function delay(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}
