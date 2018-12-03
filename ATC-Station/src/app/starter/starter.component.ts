import { Component, OnInit, OnDestroy } from '@angular/core';
import { HttpClient } from '@angular/common/http';

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


  ngOnInit() {
    // add the the body classes
    this.body.classList.add('skin-black');
    this.body.classList.add('sidebar-mini');
    this.getFlightData()
  }

  ngOnDestroy() {
    // remove the the body classes
    this.body.classList.remove('skin-black');
    this.body.classList.remove('sidebar-mini');
  }
  getFlightData(){ 
    this.http.get("https://localhost:5000/api/get_flights").subscribe(data => {
      this.flightData = data;
      console.log(data);
    })
  }

}
