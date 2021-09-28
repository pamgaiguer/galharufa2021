import { Location } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-casting',
  templateUrl: './casting.component.html',
  styleUrls: ['./casting.component.scss']
})
export class CastingComponent implements OnInit {
  sectionName: any;
  images = [62, 83, 466, 965, 982, 1043, 90, 90, 203, 965, 982, 1043].map(n => `https://picsum.photos/id/${n}/200/280?grayscale`);

  constructor(private route: ActivatedRoute, private location: Location) {}

  ngOnInit() {
    this.sectionName = this.getCastType();
  }

  getCastType(): any {
    const castingType = this.route.snapshot.routeConfig.path;
    return castingType;
  }
}
