import React from "react";
import "rc-slider/assets/index.css";
import Moment from "moment";
import Slider from "rc-slider";
import ToggleButton from "@material-ui/lab/ToggleButton";

const startingDate = Moment("1996-1-1");
const amountOfImages = 366;
const autoplayTimeout = 300;

const imageindex = [
  {
    prefix: "/images/tempplots/temp",
    blendmode: "normal",
    opacity: 0.8,
    togglevar: "enabledTemps"
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
    opacity: 1,
    togglevar: "enabledRain"
  },
  {
    prefix: "/images/skyfall/tp_0",
    blendmode: "normal",
    opacity: 1,
    togglevar: "enabledRain"
  },

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
    };
    setInterval(this.handleAutoplayTimeout.bind(this), autoplayTimeout);
    this.preloadshit();
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
          dangerouslySetInnerHTML={{ __html: this.renderSvgAsText() }}
        />

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
              selected={this.state.enabledRain}
              onChange={this.toggle("enabledRain")}
          >
            Rain
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

  preloadshit() {
    const everyimage = [];
    imageindex.forEach(imagething => {
      if (imagething.hasOwnProperty("image")) {
        let img = new Image();
        img.src = imagething.image;
        everyimage.push(img);
      } else {
        for(let i = 0; i <= amountOfImages; i++) {
          let img = new Image();
          img.src = `${imagething.prefix}${this.prefixedImgNr(i)}.png`
          everyimage.push(img);
        }
      }
    })
  }

  toggle(vari) {
    return () => {
      this.setState({ [vari]: !this.state[vari] });
    };
  }

  renderSvgAsText() {
    let output = "<svg style='width: 780px; height: 800px'>";

    imageindex.forEach(imagething => {
      if (
        imagething.hasOwnProperty("togglevar") &&
        !this.state[imagething.togglevar]
      ) {
        return;
      }
      if (imagething.hasOwnProperty("image")) {
        output += `<image href="${imagething.image}" style="mix-blend-mode: ${imagething.blendmode}; opacity: ${imagething.opacity || 1}" />`;
      } else {
        output += `<image href="${imagething.prefix}${this.prefixedImgNr()}.png" style="mix-blend-mode: ${imagething.blendmode}; opacity: ${imagething.opacity || 1}" " />`;
      }
    });
    output += "</svg>";
    return output;
  }

  toggleAutoplay() {
    this.setState({
      autoplayEnabled: !this.state.autoplayEnabled
    });
  }

  handleAutoplayTimeout() {
    if (this.state.autoplayEnabled && this.state.imageNumber < amountOfImages)
      this.setState(prevState => {
        return {
          imageNumber: prevState.imageNumber + 1,
          autoplayEnabled: prevState.imageNumber + 1 < amountOfImages
        };
      });
  }

  scrollImage(newImageNumber) {
    this.setState({
      imageNumber: newImageNumber
    });
  }

  prefixedImgNr(n) {
    n = n || this.state.imageNumber;
    return ("" + n).padStart(4, "0");
  }
}

export default App;
