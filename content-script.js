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
    .then(chart_data => {
        for (let y = 0; y < no_rows; y++) {
            for (let x = 0; x < no_cols; x++) {
                if (chart_data.data[`${x}x${y}`] < 127) {
                    rows[y].querySelectorAll(".ContributionCalendar-day")[x].setAttribute("data-level", 4);
                } else {
                    rows[y].querySelectorAll(".ContributionCalendar-day")[x].setAttribute("data-level", 0);
                }
            }
        }
    })
    .catch(err => console.error(err));

// ultimately need to do this
// rows[0].querySelector(".ContributionCalendar-day").setAttribute("data-level", 4)


