async function SubmitHabit(){
    const habit = document.getElementById("habit").value;
    const frequency = document.getElementById("frequency").value;
    const description = document.getElementById("description").value;
    const completed = document.getElementById("completed").checked;
    console.log(habit, frequency, description, completed);

    const newHabitData={
        name: habit,
        streak: parseInt(frequency),
        description: description,
    }
    console.log(newHabitData);

    const response = await fetch("http://127.0.0.1:8000/habits", {
        method: "POST",
        headers:{
            "Content-Type": "application/json"

        },
        body: JSON.stringify(newHabitData),
    });
    const data = await response.json();
    console.log("Habit added successfully",data);


}