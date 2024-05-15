import './App.css';
import Navbar from './components/Navbar';
import Footer from './components/Footer';
import Tags from './components/Tags';
import Honda from './images/honda_chevy.jpg'
import Clash from './images/clash.png'
import Osis from './images/obama_ice_spice.jpeg'


function App() {
  return (
    <div className="App">
      <header className="App-header">
        <Navbar />
        <div class="container">
            <div class="header-box">
                <h1 class="main-header" contentEditable="true" id="abt">About Me</h1>
            </div>
            <div class="p-row" id="section1">
                <p class="main-body">My name is Elijah Larios. In my free time, I usually listen to music (usually r&b or electronic) or play video games.</p>
                <div class="circular-image__container">
                    <img class="circular-image" src={Osis} alt="obama with wig"/> 
                </div>
            </div>
            <div class="p-row" id="section2">
                <p class="main-body">Clash of Clans is my main mobile game.</p>
                <img class="squircular-image" src={Clash} alt="clash of clans"/> 
            </div>
            <div class="p-row" id="section3">
                <p class="main-body">I drive a honda 🤓. Not this one though, I just found this image on google</p>
                <img class="squircular-image" src={Honda} alt="honda chevy car found on google"/> 
            </div>
            <div class="p-row" id="section4">
                <p class="main-body">Every sentence in this passage utilizes unique vocabulary, ensuring no repetition occurs. Crafting text under such constraints challenges creativity, requiring meticulous selection from an expansive lexicon. Each phrase stands alone, clear in meaning, showcasing flexibility and innovation.</p> 
            </div>
            <div class="p-row" id="section5">
                <p class="main-body">Uniqueness in expression illustrates language’s potential for endless variation, nuanced communication. Adhering to these constraints highlights the richness available within English, demonstrating adaptability as once-used words give way to synonyms or alternative constructions.</p> 
            </div>
            <div class="p-row" id="section6">
                <p class="main-body">Engaging in such exercises fosters appreciation for linguistic diversity, the art of syntax. Mastery over broad diction not only enhances writing skills but also deepens understanding across various contexts. Creative engagement with vocabulary broadens capabilities, effectively articulating complex ideas.</p> 
            </div>
            <div class="p-row" id="section6">
                <p class="main-body">In the bustling metropolis of New York City, Spider-Man swung from building to building, keeping an eye out for any signs of trouble. Meanwhile, in Gotham City, Batman was on the hunt for the elusive Joker, determined to put an end to his reign of chaos. Across the globe, Wonder Woman stood as a beacon of hope, her Lasso of Truth shining in the sunlight. Iron Man soared through the skies, his suit gleaming as he joined forces with Captain America to combat an alien threat. Over in Central City, The Flash raced through the streets, his speed unmatched by any. Not far behind, Aquaman emerged from the depths of the ocean, ready to defend his underwater kingdom. High above, Thor's hammer crackled with electricity as he prepared to battle his brother Loki. Black Panther, with the agility and strength of his namesake, patrolled the streets of Wakanda, ever vigilant. Green Lantern's ring glowed brightly as he protected the galaxy from interstellar dangers. The Scarlet Witch and Vision, a formidable duo, stood together against those who would disrupt the peace. Meanwhile, the ever-incredible Hulk, with his immense strength, was always ready to smash any obstacle in his path. And finally, the enigmatic Doctor Strange, with his mastery of the mystic arts, guarded the realm against supernatural threats. Together, these heroes from both DC and Marvel Universes exemplify the spirit of courage, justice, and unwavering determination.</p> 
            </div>

            <Tags repeatCount={3} />
            <Footer />
        </div>
      </header>
    </div>
  );
}

export default App;
