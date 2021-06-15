import { Location } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-casting',
  templateUrl: './casting.component.html',
  styleUrls: ['./casting.component.scss']
})
export class CastingComponent implements OnInit {
  sectionTitle: any;
  images = [62, 83, 466, 965, 982, 1043].map(n => `https://picsum.photos/id/${n}/410/515?grayscale`);

  constructor(private route: ActivatedRoute, private location: Location) {}

  ngOnInit(): void {
    this.sectionTitle = this.getCastType();
  }

  getCastType(): any {
    const path = this.route.snapshot.routeConfig.path;
    return path;
  }
}
