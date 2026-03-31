// calculator.js

class ScientificCalculator {
    constructor() {
        this.currentValue = 0;
        this.clear();
    }

    add(value) {
        this.currentValue += value;
    }

    subtract(value) {
        this.currentValue -= value;
    }

    multiply(value) {
        this.currentValue *= value;
    }

    divide(value) {
        if (value !== 0) {
            this.currentValue /= value;
        } else {
            console.log('Cannot divide by zero');
        }
    }

    clear() {
        this.currentValue = 0;
    }

    calculate() {
        return this.currentValue;
    }

    squareRoot() {
        this.currentValue = Math.sqrt(this.currentValue);
    }

    sine() {
        this.currentValue = Math.sin(this.currentValue);
    }

    cosine() {
        this.currentValue = Math.cos(this.currentValue);
    }

    tangent() {
        this.currentValue = Math.tan(this.currentValue);
    }
}

// Example usage:
// const calc = new ScientificCalculator();
// calc.add(5);
// calc.multiply(2);
// console.log(calc.calculate()); // Outputs 10

