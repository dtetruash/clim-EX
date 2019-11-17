import React from "react";
import "rc-slider/assets/index.css";
import Moment from "moment";
import Slider from "rc-slider";
import ToggleButton from "@material-ui/lab/ToggleButton";

const startingDate = Moment("2018-1-1");
const amountOfImages = 100;
const autoplayTimeout = 100;

const imageindex = [
  {
    prefix: "/images/tempplots/temp",
    blendmode: "normal",
    opacity: 0.8,
    togglevar: "enabledTemps"
  },
  {
    prefix: "/images/anoplots/ano",
    blendmode: "normal",
    opacity: 0.8,
    togglevar: "enabledTempsAno"
  },
  {
    prefix: "/images/ndviplots/ndvi",
    blendmode: "normal",
    opacity: 1,
    togglevar: "enabledVeg"
  },
  {
    image: "/images/heightplot/topo_only_5.png",
    blendmode: "overlay",
    opacity: 1,
    togglevar: "enabledHeithmap"
  },
  {
    prefix: "/images/riverplots/river",
    blendmode: "screen",
    opacity: 1,
    togglevar: "enabledRivers"
  },
  {
    image: "/images/borderplot/border.png",
    blendmode: "brighten"
  },
  {
    prefix: "/images/rainplots/rain",
    blendmode: "normal",
    opacity: 0.7,
    togglevar: "enabledRain"
  }
];

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      imageNumber: 1,
      autoplayEnabled: false,
      enabledHeithmap: true,
      enabledTemps: true,
      enabledRivers: true,
      enabledRain: true,
      enabledVeg: false,
      enabledTempsAno: false
    };
    setInterval(this.handleAutoplayTimeout.bind(this), autoplayTimeout);
  }

  render() {
    return (
      <div className="App">
        <div className="logo">
            <img src="/images/logos/logo.png"></img>
        </div>
        <div className="slider">
          <Slider
            onChange={this.scrollImage.bind(this)}
            min={1}
            max={amountOfImages}
            value={this.state.imageNumber}
            railStyle={{
              backgroundColor: "#3c3b3b"
            }}
            trackStyle={{
              backgroundColor: "gray"
            }}
          />
        </div>
        <div
          className="imagecontainer"
          onClick={this.toggleAutoplay.bind(this)}
        >
          <svg style={{width: "780px", height: "800px"}} dangerouslySetInnerHTML={{ __html: this.renderSvgAsText(this.state.imageNumber) }} />
        </div>

        <div className="button-controls">
          <ToggleButton
            value="check"
            selected={this.state.enabledHeithmap}
            onChange={this.toggle("enabledHeithmap")}
          >
            Heightmap
          </ToggleButton>{" "}
          &nbsp;
          <ToggleButton
            value="check"
            selected={this.state.enabledRivers}
            onChange={this.toggle("enabledRivers")}
          >
            Rivers
          </ToggleButton>
          &nbsp;
          <ToggleButton
            value="check"
            selected={this.state.enabledTemps}
            onChange={this.toggle("enabledTemps")}
          >
            Temperatures
          </ToggleButton>
          &nbsp;
          <ToggleButton
            value="check"
            selected={this.state.enabledTempsAno}
            onChange={this.toggle("enabledTempsAno")}
          >
            Temperature Anomoly
          </ToggleButton>
          &nbsp;
          <ToggleButton
              value="check"
              selected={this.state.enabledRain}
              onChange={this.toggle("enabledRain")}
          >
            Rain
          </ToggleButton>
        &nbsp;
          <ToggleButton
              value="check"
              selected={this.state.enabledVeg}
              onChange={this.toggle("enabledVeg")}
          >
            Vegetation
          </ToggleButton>
        </div>

        <span className="metadata">
          {Moment(startingDate)
            .add(this.state.imageNumber - 1, "day")
            .format("DD MMM YYYY")}
        </span>
      </div>
    );
  }

  toggle(vari) {
    return () => {
      //if (vari !== "enableTemps" && vari !== "enableTempsAno" && vari !== "enableVeg") {
          this.setState({[vari]: !this.state[vari]})
       /* }
      else if(this.state[vari]) {
          this.setState({[vari]: false})
        }
        else {
         let newThing =  {
            ebableTemps: false,
            ebableTempsAno: false,
            ebableVeg: false
          }
          newThing[vari] = true;

          this.setState(newThing)
        } */
    };
  }

  renderSvgAsText(n) {
    let output = "";
    imageindex.forEach(imagething => {
      if (!this.imagethingIsVisable(imagething)) {
        return;
      }
      if (imagething.hasOwnProperty("image")) {
        output += `<image href="${imagething.image}" style="mix-blend-mode: ${imagething.blendmode}; opacity: ${imagething.opacity || 1}" />`;
      } else {
        output += `<image href="${imagething.prefix}${this.prefixedImgNr(n)}.png" style="mix-blend-mode: ${imagething.blendmode}; opacity: ${imagething.opacity || 1}" " />`;
      }
    });
    return output;
  }

  imagethingIsVisable(imagething) {
    return !imagething.hasOwnProperty("togglevar") || this.state[imagething.togglevar]
  }

  toggleAutoplay() {
    this.setState({
      autoplayEnabled: !this.state.autoplayEnabled
    });
  }

  handleAutoplayTimeout() {
    if (this.state.autoplayEnabled && this.state.imageNumber < amountOfImages) {
      this.setCurrentImageThing(this.state.imageNumber+1);
      if(this.state.imageNumber + 1 >= amountOfImages) {
        this.setState({
          autoplayEnabled: false
        });
      }
    }
  }

  setCurrentImageThing(n) {
    let loadedImages = 0;
    let targetImageThing = 0;
    let loadCallback = () => {
      loadedImages++;
      if(loadedImages === targetImageThing) {
        this.setState({
          imageNumber: n
        });
      }
    };

    imageindex.forEach(imagething => {
      if (!this.imagethingIsVisable(imagething)) {
        return;
      }
      const primaryImage = new Image();
      primaryImage.onload = loadCallback;
      targetImageThing++;
      if (imagething.hasOwnProperty("image")) {
        primaryImage.src = imagething.image;
      } else {
        primaryImage.src += imagething.prefix + this.prefixedImgNr(n) + ".png"
      }
    });
  }

  scrollImage(newImageNumber) {
    this.setCurrentImageThing(newImageNumber)
  }

  prefixedImgNr(n) {
    return ("" + n).padStart(4, "0");
  }
}

export default App;
