import { Component, OnInit, OnDestroy } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs/Rx';
import 'rxjs/add/observable/interval';

@Component({
  selector: 'app-starter',
  templateUrl: './starter.component.html',
  styleUrls: ['./starter.component.css']
})
export class StarterComponent implements OnInit, OnDestroy {

  private flightData;
  bodyClasses = 'skin-black sidebar-mini';
  body: HTMLBodyElement = document.getElementsByTagName('body')[0];

  constructor(private http: HttpClient) { }
  private url: string = "";

  ngOnInit() {
    // add the the body classes
    this.body.classList.add('skin-black');
    this.body.classList.add('sidebar-mini');
    this.getFlightData();
    Observable.interval(20000).subscribe(x => this.getFlightData());
    document.getElementById("tweets").innerHTML = '<iframe src="https://www.csc2.ncsu.edu/faculty/healey/tweet_viz/tweet_app/?q=' + 'American Airlines OR United Airlines' + '" width="100%" height="500px;" id ="myiframe" ></iframe>';


  }

  ngOnDestroy() {
    // remove the the body classes
    this.body.classList.remove('skin-black');
    this.body.classList.remove('sidebar-mini');
  }

  setTweets() {
    console.log("URL: " + this.url);
    document.getElementById("tweets").innerHTML = '<iframe src="https://www.csc2.ncsu.edu/faculty/healey/tweet_viz/tweet_app/?q=' + this.url + '" width="100%" height="500px;" id ="myiframe" ></iframe>';
  }


  getFlightData() {
    this.http.get("http://localhost:1337/api/get_flights").subscribe(data => {
      this.flightData = data;
      var airlines = []
      //console.log(this.flightData);
      let foundFlights = "";
      for (let i = 0; i < 20; i++) {
        let currAircraft = this.flightData[i]['aircraft'];
        if (currAircraft !== undefined && currAircraft.length !== 0) {
          for (let j = 0; j < 10; j++) {
            if (currAircraft[j] !== undefined && currAircraft[j]['flight'] !== undefined && currAircraft[j]['flight'] !== "") {
              // foundFlights += currAircraft[j]['flight'] + " OR ";
              this.http.get("http://localhost:1337/api/airline/" + currAircraft[j]['flight'].substring(0, 3)).subscribe(data2 => {
                if (data2['name'].length > 0) {
                  // console.log("Found airline: " + data2['name'] + " with code: " + currAircraft[j]['flight']);
                  if (!airlines.includes(data2['name'])) {
                    airlines.push(data2['name']);
                    for (let i = 0; i < airlines.length; i++) {
                      this.url += airlines[i] + " OR ";
                    }

                  }
                }
              })
            }
          }

        }
      }
      console.log("URL: " + this.url);

      document.getElementById("tweets").innerHTML = '<iframe src="https://www.csc2.ncsu.edu/faculty/healey/tweet_viz/tweet_app/?q=' + this.url + '" width="100%" height="500px;" id ="myiframe" ></iframe>';


      // this.setTweets();

      /*
      var url = "";
      for (let i = 0; i < airlines.length; i++) {
        url += airlines[i] + " OR ";
      }*/
      // Airline code to airline

      // document.getElementById("tweets").innerHTML = '<iframe src="https://www.csc2.ncsu.edu/faculty/healey/tweet_viz/tweet_app/?q=' + url + '" width="100%" height="500px;" id ="myiframe" ></iframe>';

      // document.getElementById("weather").innerText = this.flightData;
      // console.log(data);
    })
  }

}
