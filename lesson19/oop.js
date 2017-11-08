;(function (global) {
    "use strict";

    function Person(name) {
        this.name = name;
    }

    Person.prototype.getName = function () {
        return this.name;
    };

    Person.prototype.setName = function (name) {
        return this.name = name;
    };

    function Developer(name, skills) {
        Person.call(this, name); // apply(context)
        this.skills = skills || [];
    }

    Developer.prototype = Object.create(Person.prototype);

    Developer.prototype.getSkills = function () {
        return this.skills;
    };

    var linus = new Person('Linus');
    console.log(linus.getName())
})(Window);
