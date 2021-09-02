let app = new Vue({
    el: '#app',
    data: {
        inputTempNum: '0.0',
        tempList: ['Farenheit', 'Celsius', 'Kelvin'],
        startingUnit: 'Farenheit',
        requestedUnit: 'Celsius',
        convertedUnit: '',
    }, methods: {
        tempConversion: function () {
            let converter = {
                    "to celsius": [{
                        'Farenheit': ((this.inputTempNum - 32) * 5 / 9),
                        'Kelvin': (this.inputTempNum - 273.15)
                    }],
                    "to output": [{
                        'Farenheit': ((this.inputTempNum * 9 / 5) + 32),
                        'Kelvin': (this.inputTempNum + 273.15)
                    }]
                }
            
            // //from celsius to farenheit
            // if (this.startingUnit == 'Celsius' && this.requestedUnit == 'Farenheit') {
            //     output = ((this.inputTempNum * 9 / 5) + 32)
            //     this.convertedUnit = (Math.round(output * 10) / 10)
            // }
            // //from kelvin to farenheit
            // else if (this.startingUnit == 'Kelvin' && this.requestedUnit == 'Farenheit') {
            //     output = (((this.inputTempNum - 273.15 - 273.15) * 9 / 5) + 32)
            //     this.convertedUnit = (Math.round(output * 10) / 10)
            // }
            // //from farenheit to farenheit
            // else if (this.startingUnit == 'Farenheit' && this.requestedUnit == 'Farenheit') {
            //     this.convertedUnit = this.inputTempNum
            // }

            // //from farenheit to celsius
            // else if (this.startingUnit == 'Farenheit' && this.requestedUnit == 'Celsius') {
            //     output = ((this.inputTempNum - 32) * 5 / 9)
            //     this.convertedUnit = (Math.round(output * 10) / 10)
            // }
            // //from kelvin to celsius
            // else if (this.startingUnit == 'Kelvin' && this.requestedUnit == 'Celsius') {
            //     output = (this.inputTempNum - 273.15)
            //     this.convertedUnit = (Math.round(output * 10) / 10)
            // }
            // //from celsius to celsius
            // else if (this.startingUnit == 'Celsius' && this.requestedUnit == 'Celsius') {
            //     this.convertedUnit = this.inputTempNum
            // }

            // //from farenheit to kelvin
            // else if (this.startingUnit == 'Farenheit' && this.requestedUnit == 'Kelvin') {
            //     output = (((this.inputTempNum - 32) * 5 / 9) + 273.15)
            //     this.convertedUnit = (Math.round(output * 10) / 10)
            // }
            // //from celsius to kelvin
            // else if (this.startingUnit == 'Celsius' && this.requestedUnit == 'Kelvin') {
            //     output = (this.inputTempNum + 273.15)
            //     this.convertedUnit = (Math.round(output * 10) / 10)
            // }
            // //from celsius to celsius
            // else {
            //     this.convertedUnit = this.inputTempNum
            // }
        }
    }
})