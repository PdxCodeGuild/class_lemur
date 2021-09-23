


let app = new Vue({
    el: '#app',
    // data is where Vue holds variables that can be used in both the html file, and in the methods portion. Essentially, these allow Vue.js to instantly communicate with your html file. 

    data: {
        //Rendering from Vue
        // The html page will render this by placing the value in {{ double curly braces }}
        sayHello: 'Hello from Vue!!',

        //Text Input
        // userName is a blank value waiting on input from the user through v-model
        userName: '',

        //Select and Options (Dynamic) list
        colors: ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet'],

        //Select and Options (Dynamic) selected color
        // Chosen color from the colors(line 13) list; it can be initially set to any value from the colors list like it currently is, hard-coded into the html (only recommended for a value that will be disabled as soon as the select is clicked on), or left blank to leave the dropdown blank until clicked on.
        chosenColorDynamic: 'Yellow',

        //Select and Options (Hard-Coded)
        // The value for chosenColorStatic is hard-coded into the html, and will only be sent here if the user interacts with the select. If 'Please select one' wasn't hard-coded into the html list, the select would be blank until clicked on.
        chosenColorStatic: '',

        //Radio Buttons (Dynamic) list
        // The html will use a v-for loop to iterate over the animals list, and render a radio button for each one
        animals: ['Quokka', 'Sugar Glider', 'Mantis Shrimp'],
        //Radio Buttons (Dynamic) selection
        // chosenRadioAnimalDynamic will initially check the radio button for Sugar Glider. If this were left blank, none of the boxes would be check when the page loads/refreshes.
        chosenRadioAnimalDynamic: 'Sugar Glider',

        //Radio Buttons (Hard-Coded)
        // Since all three radio buttons (cats, dogs, velociraptor) are hard-coded into the html, chosenRadioAnimalStatic is waiting for user input to be changed. Since we wrote 'Velociraptor' here, its button will already be checked when the page loads/refreshes.
        chosenRadioAnimalStatic: 'Velociraptor',

        //Rendering From a List of Dictionaries
        // contacts holds a list of dictionaries that we can render in html. See the notes in vue_example.html to learn how to do it.
        contacts: [{
            name: 'John Doe',
            phoneNumber: '805-867-5309'
        }, {
            name: 'Jane Doe',
            phoneNumber: '775-423-2315'
        }, {
            name: 'Keanu Reeves',
            phoneNumber: '503-335-4816'
        }],

        //Checkboxes
        // A checkbox is a boolean, so an empty string will leave the box unchecked, and anything (including a whitespace) will check the box.
        // If you want the user to be able to check multiple boxes at once and grab their individual values, they each need their own data variable. 
        checkMePlease: '',
        uncheckMePlease: 'make this truthy',
        // If the user checks one box, all other boxes that are bound to this variable will also be checked.
        checkTwo: '',
        // The redFruits list will be used to generate multiple checkboxes
        redFruits: ['Cherries', 'Strawberries', 'Apples', 'Watermelon'],
        // As the user checks and unchecks boxes, their values will be added and removed accordingly.
        checkedRedFruits: [],
        //Because the green fruits are hard-coded into the html, we only need a blank list to catch the selections
        checkedGreenFruits: [],

        //these values act just like the others in our data. The only difference is that these are used in methods on this particular document. Look at the functions below to see how they work.
        //calculate()
        firstNum: 0.0,
        secondNum: 0.0,
        answer: 0.0,

        //tempConversion()
        inputTempNum: '',
        tempList: ['Farenheit', 'Celsius', 'Kelvin'],
        startingUnit: 'Farenheit',
        requestedUnit: 'Celsius',
        convertedNum: '',
        inCelsius: '',

    },
    // methods is where you'll write your actual javaScript code. You can use the variables from data to get information from your user through the html file. Note that arrow functions will not work here. 
    methods: {
        calculate: function () {
            //to refer to our data variables, all we have to do is add this. before it. Since our functions change the variables being rendered, we don't need to return anything (Vue essentially does it for you). So to refer to firstNum, we would say this.firstNum.
            this.answer = parseFloat(this.firstNum) + parseFloat(this.secondNum)
        },
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