async function main () {
  graph(0, [], [], 0);

  resp = await $.post("https://whqqnvb6ge.execute-api.eu-central-1.amazonaws.com/prod/git-stats", JSON.stringify({link: "https://github.com/users/mathisco-01/contributions",granularity: 7}));
  graph(resp.total, resp.data.count, resp.data.date, 5);



};

function graph(total, data, labels, labelGranularity) {
  var ctx = document.getElementById('myChart').getContext('2d');
  var lineChart = new Chart(ctx, {
    type: 'line',
    data: {
      labels: labels,
      datasets: [{
        data: data,
        backgroundColor: [
             'rgba(0, 102, 255, 0.2)',
         ],
       borderColor: [
         'rgba(0, 51, 204, 1)',
       ],
      }],
    },
    options: {
      title: {
        display: true,
        text: `${total} Git contributions in the past year`
      },
      legend: {
        display: false,
      },
      scales: {
        xAxes: [{
          ticks: {
            maxTicksLimit: data.length / labelGranularity
          }
        }]
      }
    }
  })
};
