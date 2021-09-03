


let app = new Vue({
    el: '#app',
    data: {
        inputTempNum: '',
        tempList: ['Farenheit', 'Celsius', 'Kelvin'],
        startingUnit: 'Farenheit',
        requestedUnit: 'Celsius',
        convertedNum: '',
        inCelsius: '',
    },
    methods: {
        tempConversion: function () {
            let converter =
            {
                "toCelsius": {
                    'Farenheit': ((parseFloat(this.inputTempNum) - 32) * 5 / 9),
                    'Kelvin': (parseFloat(this.inputTempNum) - 273.15),
                    'Celsius': parseFloat(this.inputTempNum)
                }
            }
            let inCelsius = converter['toCelsius'][this.startingUnit]
            let outputConverter =
            {
                "toOutput": {
                    'Farenheit': ((parseFloat(inCelsius) * 9 / 5) + 32),
                    'Kelvin': (parseFloat(inCelsius) + 273.15),
                    'Celsius': parseFloat(inCelsius),
                }
            }
            this.convertedNum = Math.round(outputConverter['toOutput'][this.requestedUnit] * 10) / 10
        }
    }
})