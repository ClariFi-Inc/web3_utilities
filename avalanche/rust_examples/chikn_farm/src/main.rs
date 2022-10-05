use reqwest;
use serde::{Deserialize, Serialize};

#[tokio::main]
async fn main() {
    // chaining .await will yield our query result
    let result = reqwest::get("https://api.chikn.farm/api/farmland/details/{231}")
        .await
        .unwrap()
        .text()
        .await;
    println!("{:?}", result)
}
