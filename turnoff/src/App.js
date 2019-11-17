import React from "react";
import "rc-slider/assets/index.css";
import Moment from "moment";
import Slider from "rc-slider";
import ToggleButton from "@material-ui/lab/ToggleButton";

const startingDate = Moment("1996-1-1");
const amountOfImages = 5;
const autoplayTimeout = 50;

const imageindex = [
  {
    prefix: "tempplots/temp",
    blendmode: "normal",
    opacity: 0.8,
    togglevar: "enabledTemps"
  },
  {
    image: "/images/heightmap-akatopo.png",
    blendmode: "overlay",
    opacity: 1,
    togglevar: "enabledHeithmap"
  },
  {
    prefix: "riverplots/river",
    blendmode: "screen",
    opacity: 1,
    togglevar: "enabledRivers"
  },
  {
    image: "/images/borderplot/border.png",
    blendmode: "normal"
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
      enabledRivers: true
    };
    setInterval(this.handleAutoplayTimeout.bind(this), autoplayTimeout);
  }

  render() {
    return (
      <div className="App">
        <div className="logo">
            <img src="/images/logos/readme-banner.png"></img> 
        </div>
        <div className="slider">
          <Slider
            onChange={this.scrollImage.bind(this)}
            min={1}
            max={amountOfImages}
            value={this.state.imageNumber}
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
            Toggle Heightmap
          </ToggleButton>{" "}
          &nbsp;
          <ToggleButton
            value="check"
            selected={this.state.enabledRivers}
            onChange={this.toggle("enabledRivers")}
          >
            Toggle Rivers
          </ToggleButton>
          &nbsp;
          <ToggleButton
            value="check"
            selected={this.state.enabledTemps}
            onChange={this.toggle("enabledTemps")}
          >
            Toggle Temperatures
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
        output += `<image href="${imagething.image}" style="mix-blend-mode: ${
          imagething.blendmode
        }; opacity: ${imagething.opacity || 1}" />`;
      } else {
        output += `<image href="/images/${
          imagething.prefix
        }${this.prefixedImgNr()}.png" style="mix-blend-mode: ${
          imagething.blendmode
        }; opacity: ${imagething.opacity || 1}" " />`;
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

  prefixedImgNr() {
    return ("" + this.state.imageNumber).padStart(4, "0");
  }
}

export default App;
