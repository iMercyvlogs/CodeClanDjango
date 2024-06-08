const titleInput=document.querySelector('input[name=title]');
// create a constant that dynamically queries the title and slug of the created item/post
const slugInput=document.querySelector('input[name=slug]')

//now create a constant which is a function that accepts a value , changes it to a slug, then returns a slug

const slugify=(val)=>{
    return val.toString().toLowerCase().trim()  //convert entry to string, then to lowercase, then delete all empty spaces
    .replace(/&/g,'-and-') //replace & with'-and-'
    .replace(/[\s\W-]+/g, '-')  //replace spaces with hyphen
};

titleInput.addEventListener('keyup',(e)=>{  //add event listener 'keyup'
    //what happens after the key has been pressed
    slugInput.setAttribute('value', slugify(titleInput.value))  //the attribute of this event is "value", it should be passed into the slugify function
    //
});