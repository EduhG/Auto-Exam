$(document).ready(function(){
    $('input').iCheck({
        checkboxClass: 'icheckbox_flat',
        radioClass: 'iradio_flat'
    });


    $("select2").select2({
        /*placeholder: "Select a state",
        allowClear: true*/
    });

    // Materialize.updateTextFields();
});

var MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
var randomScalingFactor = function() {
    return Math.round(Math.random() * 100 * (Math.random() > 0.5 ? -1 : 1));
};
var randomColorFactor = function() {
    return Math.round(Math.random() * 255);
};
var randomColor = function(opacity) {
    return 'rgba(' + randomColorFactor() + ',' + randomColorFactor() + ',' + randomColorFactor() + ',' + (opacity || '.3') + ')';
};

var config = {
    type: 'line',
    data: {
        labels: ["Maths", "English", "Kiswahili", "Science", "Social Studies"],
        datasets: [{
            label: "First Term",
            data: [80, 65, 70, 80, 76],
            fill: false,
            borderDash: [5, 5],
        }, {
            label: "Second Term",
            data: [74, 75, 80, 70, 86],
            fill: false,
            borderDash: [5, 5],
        }, {
            label: "Third Term",
            data: [90, 80, 50, 73, 69],
            fill: false,
        }]
    },
    options: {
        responsive: true,
        legend: {
            position: 'bottom',
        },
        hover: {
            mode: 'label'
        },
        scales: {
            xAxes: [{
                display: true,
                scaleLabel: {
                    display: true,
                    labelString: 'Month'
                }
            }],
            yAxes: [{
                display: true,
                scaleLabel: {
                    display: true,
                    labelString: 'Marks'
                }
            }]
        },
        title: {
            display: false,
            text: 'Chart.js Line Chart - Legend'
        }
    }
};

$.each(config.data.datasets, function(i, dataset) {
    var background = randomColor(0.5);
    dataset.borderColor = background;
    dataset.backgroundColor = background;
    dataset.pointBorderColor = background;
    dataset.pointBackgroundColor = background;
    dataset.pointBorderWidth = 1;
});

window.onload = function() {

};


var randomScalingFactor1 = function() {
        return (Math.random() > 0.5 ? 1.0 : -1.0) * Math.round(Math.random() * 100);
    };
    var randomColorFactor1 = function() {
        return Math.round(Math.random() * 255);
    };
    var randomColor = function() {
        return 'rgba(' + randomColorFactor1() + ',' + randomColorFactor1() + ',' + randomColorFactor1() + ',.7)';
    };

    var barChartData = {
        labels: ["Maths", "English", "Kiswahili", "Science", "Social Studies"],
        datasets: [{
            label: '',
            backgroundColor: randomColor(), //"rgba(220,220,220,0.5)",
            data: [80, 65, 70, 85, 76]
        }]

    };
    window.onload = function() {
        var ctx = document.getElementById("buyers").getContext("2d");
        window.myLine = new Chart(ctx, config);

        var termly = document.getElementById("termly").getContext("2d");
        window.myBar = Chart.Bar(termly, {
            data: barChartData,
            options: {
                legend: {
                    display: false,
                },
                responsive: true,
                hoverMode: 'label',
                hoverAnimationDuration: 400,
                stacked: false,
                title:{
                    display:false,
                    //text:"Chart.js Bar Chart - Multi Axis"
                },
                scales: {
                    yAxes: [{
                        type: "linear", // only linear but allow scale type registration. This allows extensions to exist solely for log scale for instance
                        display: true,
                        position: "left",
                        id: "y-axis-1",
                    }],
                }
            }
        });
    };


$('#sidenav>ul').on('click', '.submenu', function (e) {
    console.log('hey you');
    var element = $(this);//.parent('li');

    if (element.hasClass('open')) {
        element.removeClass('open');
        element.find('li').removeClass('open');
        element.find('ul').slideUp();
    }
    else {
        element.addClass('open');
        element.children('ul').slideDown();
        element.siblings('li').children('ul').slideUp();
        element.siblings('li').removeClass('open');
        element.siblings('li').find('li').removeClass('open');
        element.siblings('li').find('ul').slideUp();
    }

    if ($(this).attr('href') == '#') {
        e.preventDefault();
    }

});