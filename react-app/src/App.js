import './App.css';
import Navbar from './components/Navbar';
import Footer from './components/Footer';
import Honda from './images/honda_chevy.jpg'
import Clash from './images/clash.png'
import Osis from './images/obama_ice_spice.jpeg'
// https://firebase.google.com/docs/web/setup#available-libraries
// import { initializeApp } from "firebase/app";
// import { getAnalytics } from "firebase/analytics";
// import { getFirestore } from "firebase/firestore";


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
             <Footer />
        </div>
      </header>
    </div>
  );
}

export default App;
