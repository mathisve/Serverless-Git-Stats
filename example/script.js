async function main() {
  graph(0, [], [], 0, 0);

  const url = "https://whqqnvb6ge.execute-api.eu-central-1.amazonaws.com/prod/git-stats";
  resp = await fetch(url)
      .then((res) => {
        if(res.status == 200) {
            return res.json();   //works just fine
        }
      })
      .catch(error => console.log(error.message));

  var dataLength = resp.data.count.length
  var newData = [];
  var newLabels = [];

  const dataGranularity = 5;
  const labelGranularity = dataLength/dataGranularity/10;

  for (i = 0; i < dataLength; i++) {
    if (i % dataGranularity == 0) {
      newData.push(resp.data.count[i]);
      newLabels.push(resp.data.date[i]);
    }
  }

  graph(dataLength, newData, newLabels, dataGranularity, labelGranularity);

function graph(dataLength, data, labels, dataGranularity, labelGranularity) {
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
          text: `${dataLength} Git contributions in the past year`
        },
        legend: {
          display: false,
        },
        scales: {
          xAxes: [{
            ticks: {
              maxTicksLimit: labelGranularity
            }
          }]
        }
      }
    })
  };
}
